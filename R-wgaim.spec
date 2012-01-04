%global packname  wgaim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Whole Genome Average Interval Mapping for QTL detection using mixed models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-qtl R-lattice 

BuildRequires:    R-devel tex(latex) R-qtl R-lattice 

%description
This package integrates sophisticated mixed modelling methods with a whole
genome approach to detecting significant QTL's in linkage maps.

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
%doc %{rlibdir}/wgaim/html
%doc %{rlibdir}/wgaim/CITATION
%doc %{rlibdir}/wgaim/DESCRIPTION
%{rlibdir}/wgaim/help
%{rlibdir}/wgaim/Meta
%{rlibdir}/wgaim/data
%{rlibdir}/wgaim/R
%{rlibdir}/wgaim/extdata
%{rlibdir}/wgaim/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora