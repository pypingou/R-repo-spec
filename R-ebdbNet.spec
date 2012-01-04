%global packname  ebdbNet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Empirical Bayes Estimation of Dynamic Bayesian Networks

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package is used to infer the adjacency matrix of a network from time
course data using an empirical Bayes estimation procedure based on Dynamic
Bayesian Networks.

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
%doc %{rlibdir}/ebdbNet/html
%doc %{rlibdir}/ebdbNet/NEWS
%doc %{rlibdir}/ebdbNet/DESCRIPTION
%{rlibdir}/ebdbNet/help
%{rlibdir}/ebdbNet/R
%{rlibdir}/ebdbNet/NAMESPACE
%{rlibdir}/ebdbNet/Meta
RPM build errors:
%{rlibdir}/ebdbNet/libs
%{rlibdir}/ebdbNet/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora