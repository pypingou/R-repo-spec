%global packname  KCsmart
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.12.0
Release:          1%{?dist}
Summary:          Multi sample aCGH analysis package using kernel convolution

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-siggenes R-multtest R-KernSmooth 


BuildRequires:    R-devel tex(latex) R-methods R-siggenes R-multtest R-KernSmooth



%description
Multi sample aCGH analysis package using kernel convolution

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
%doc %{rlibdir}/KCsmart/DESCRIPTION
%doc %{rlibdir}/KCsmart/html
%doc %{rlibdir}/KCsmart/doc
%{rlibdir}/KCsmart/data
%{rlibdir}/KCsmart/Meta
%{rlibdir}/KCsmart/R
%{rlibdir}/KCsmart/NAMESPACE
%{rlibdir}/KCsmart/INDEX
%{rlibdir}/KCsmart/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12.0-1
- initial package for Fedora