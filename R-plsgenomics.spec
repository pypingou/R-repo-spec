%global packname  plsgenomics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          PLS analyses for genomics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
This package provides routines for PLS-based genomic analyses. It
implements PLS methods for classification with microarray data and
prediction of transcription factor activities from combined ChIP-chip
analysis. The >=1.2-1 versions include two new classification methods for
microarray data: GSIM and Ridge PLS.

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
%doc %{rlibdir}/plsgenomics/html
%doc %{rlibdir}/plsgenomics/DESCRIPTION
%{rlibdir}/plsgenomics/Meta
%{rlibdir}/plsgenomics/data
%{rlibdir}/plsgenomics/R
%{rlibdir}/plsgenomics/NAMESPACE
%{rlibdir}/plsgenomics/help
%{rlibdir}/plsgenomics/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.6-1
- initial package for Fedora