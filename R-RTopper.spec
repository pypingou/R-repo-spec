%global packname  RTopper
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          This package is designed to perform Gene Set Analysis across multiple genomic platforms

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-limma R-multtest 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-limma R-multtest 


%description
the RTopper package is designed to perform and integrate gene set
enrichment results across multiple genomic platforms.

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
%doc %{rlibdir}/RTopper/DESCRIPTION
%doc %{rlibdir}/RTopper/CITATION
%doc %{rlibdir}/RTopper/doc
%doc %{rlibdir}/RTopper/html
%{rlibdir}/RTopper/help
%{rlibdir}/RTopper/data
%{rlibdir}/RTopper/NAMESPACE
%{rlibdir}/RTopper/Meta
%{rlibdir}/RTopper/INDEX
%{rlibdir}/RTopper/R
%{rlibdir}/RTopper/LICENSE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora