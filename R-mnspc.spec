%global packname  mnspc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          Multivariate Nonparametric Statistical Process Control

Group:            Applications/Engineering 
License:          X11
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Statistical process control for multivariate data that is not necessarily
Gaussian distributed. A function is provided to categorize components of
multivariate response vectors. Tools for setting up a CUSUM procedure for
the transformed data are included. The CUSUM scheme can also be applied to
the case when some (or all) of the multivariate response components are

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
%doc %{rlibdir}/mnspc/html
%doc %{rlibdir}/mnspc/DESCRIPTION
%{rlibdir}/mnspc/Meta
%{rlibdir}/mnspc/libs
%{rlibdir}/mnspc/NAMESPACE
RPM build errors:
%{rlibdir}/mnspc/help
%{rlibdir}/mnspc/data
%{rlibdir}/mnspc/INDEX
%{rlibdir}/mnspc/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora