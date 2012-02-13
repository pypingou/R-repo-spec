%global packname  nleqslv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.2
Release:          1%{dist}
Summary:          Solve systems of non linear equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Solve a system of non linear equations using a Broyden or a Newton method
with a choice of global strategies such as linesearch and trust region.
There are options for using a numerical or an analytical jacobian and
fixed or automatic scaling of parameters.

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
%doc %{rlibdir}/nleqslv/NEWS
%doc %{rlibdir}/nleqslv/DESCRIPTION
%doc %{rlibdir}/nleqslv/html
%{rlibdir}/nleqslv/help
%{rlibdir}/nleqslv/NAMESPACE
%{rlibdir}/nleqslv/INDEX
%{rlibdir}/nleqslv/Meta
%{rlibdir}/nleqslv/R
%{rlibdir}/nleqslv/libs

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.2-1
- Update to version 1.9.2

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.0-1
- initial package for Fedora