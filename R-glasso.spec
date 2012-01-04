%global packname  glasso
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Graphical lasso- estimation of Gaussian graphical models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Graphical lasso

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
%doc %{rlibdir}/glasso/html
%doc %{rlibdir}/glasso/DESCRIPTION
%{rlibdir}/glasso/R
%{rlibdir}/glasso/libs
%{rlibdir}/glasso/NAMESPACE
%{rlibdir}/glasso/help
%{rlibdir}/glasso/Meta
%{rlibdir}/glasso/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7-1
- initial package for Fedora