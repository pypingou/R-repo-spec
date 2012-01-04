%global packname  lol
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Lots Of Lasso

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-penalized R-Matrix 

BuildRequires:    R-devel tex(latex) R-penalized R-Matrix 

%description
Various optimization methods for Lasso inference with matrix warpper

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
%doc %{rlibdir}/lol/doc
%doc %{rlibdir}/lol/html
%doc %{rlibdir}/lol/DESCRIPTION
%{rlibdir}/lol/NAMESPACE
%{rlibdir}/lol/data
%{rlibdir}/lol/INDEX
%{rlibdir}/lol/help
%{rlibdir}/lol/Meta
%{rlibdir}/lol/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora