%global packname  dfoptim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.8.1
Release:          1%{?dist}
Summary:          Derivative-free Optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Derivative-Free optimization algorithms. These algorithms do not require
gradient information. More importantly, they can be used to solve
non-smooth optimization problems.

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
%doc %{rlibdir}/dfoptim/html
%doc %{rlibdir}/dfoptim/NEWS
%doc %{rlibdir}/dfoptim/DESCRIPTION
%{rlibdir}/dfoptim/help
%{rlibdir}/dfoptim/NAMESPACE
%{rlibdir}/dfoptim/Meta
%{rlibdir}/dfoptim/R
%{rlibdir}/dfoptim/demo
%{rlibdir}/dfoptim/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.8.1-1
- initial package for Fedora