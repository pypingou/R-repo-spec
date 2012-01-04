%global packname  dlmap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.07
Release:          1%{?dist}
Summary:          Detection Localization Mapping for QTL

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-qtl R-ibdreg R-wgaim R-nlme R-mgcv 

BuildRequires:    R-devel tex(latex) R-qtl R-ibdreg R-wgaim R-nlme R-mgcv 

%description
QTL mapping in a mixed model framework with separate detection and
localization stages. The first stage detects the number of QTL on each
chromosome based on the genetic variation due to grouped markers on the
chromosome; the second stage uses this information to determine the most
likely QTL positions. The mixed model can accommodate general fixed and
random effects, including spatial effects in field trials and pedigree
effects. Applicable to backcrosses, doubled haploids, recombinant inbred
lines, F2 intercrosses, and association mapping populations.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/dlmap/CITATION
%doc %{rlibdir}/dlmap/html
%doc %{rlibdir}/dlmap/DESCRIPTION
%{rlibdir}/dlmap/INDEX
%{rlibdir}/dlmap/help
%{rlibdir}/dlmap/data
%{rlibdir}/dlmap/Meta
%{rlibdir}/dlmap/NAMESPACE
%{rlibdir}/dlmap/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.07-1
- initial package for Fedora