%global packname  far
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.3
Release:          1%{?dist}
Summary:          Modelization for Functional AutoRegressive processes

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
Modelizations and previsions functions for Functional AutoRegressive
processes using nonparametric methods: functional kernel, estimation of
the covariance operator in a subspace, ...

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
%doc %{rlibdir}/far/DESCRIPTION
%doc %{rlibdir}/far/html
%doc %{rlibdir}/far/NEWS
%{rlibdir}/far/NAMESPACE
%{rlibdir}/far/R
%{rlibdir}/far/help
%{rlibdir}/far/INDEX
%{rlibdir}/far/libs
%{rlibdir}/far/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.3-1
- initial package for Fedora