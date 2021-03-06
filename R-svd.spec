%global packname  svd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Interfaces to various state-of-art SVD and eigensolvers

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides various R bindings to various SVD and eigensolvers
(PROPACK, nuTRLan)

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
%doc %{rlibdir}/svd/html
%doc %{rlibdir}/svd/DESCRIPTION
%{rlibdir}/svd/LICENSE
%{rlibdir}/svd/include
%{rlibdir}/svd/NAMESPACE
%{rlibdir}/svd/INDEX
%{rlibdir}/svd/Meta
%{rlibdir}/svd/help
%{rlibdir}/svd/libs
%{rlibdir}/svd/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora