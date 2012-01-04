%global packname  dbEmpLikeGOF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Goodness-of-fit and two sample comparison tests using sample entropy

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Goodness-of-fit and two sample comparison tests using sample entropy

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
%doc %{rlibdir}/dbEmpLikeGOF/doc
%doc %{rlibdir}/dbEmpLikeGOF/DESCRIPTION
%doc %{rlibdir}/dbEmpLikeGOF/html
%{rlibdir}/dbEmpLikeGOF/Meta
%{rlibdir}/dbEmpLikeGOF/NAMESPACE
%{rlibdir}/dbEmpLikeGOF/data
%{rlibdir}/dbEmpLikeGOF/INDEX
%{rlibdir}/dbEmpLikeGOF/R
%{rlibdir}/dbEmpLikeGOF/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora