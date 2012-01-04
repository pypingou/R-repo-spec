%global packname  glpk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.8.0.5
Release:          1%{?dist}
Summary:          GNU Linear Programming Kit

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.8-0.5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The GNU Linear Programming Kit (GLPK) version 4.8.  This interface mirrors
the GLPK C API.  Almost all GLPK lpx routines are supported.

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
%doc %{rlibdir}/glpk/html
%doc %{rlibdir}/glpk/doc
%doc %{rlibdir}/glpk/DESCRIPTION
%{rlibdir}/glpk/R
%{rlibdir}/glpk/help
%{rlibdir}/glpk/INDEX
%{rlibdir}/glpk/libs
%{rlibdir}/glpk/NAMESPACE
RPM build errors:
%{rlibdir}/glpk/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.8.0.5-1
- initial package for Fedora