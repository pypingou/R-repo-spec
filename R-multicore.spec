%global packname  multicore
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Parallel processing of R code on machines with multiple cores or CPUs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a way of running parallel computations in R on
machines with multiple cores or CPUs. Jobs can share the entire initial
workspace and it provides methods for results collection.

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
%doc %{rlibdir}/multicore/html
%doc %{rlibdir}/multicore/NEWS
%doc %{rlibdir}/multicore/DESCRIPTION
%{rlibdir}/multicore/libs
%{rlibdir}/multicore/R
%{rlibdir}/multicore/help
%{rlibdir}/multicore/Meta
%{rlibdir}/multicore/NAMESPACE
%{rlibdir}/multicore/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora