%global packname  fun
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Use R for Fun

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This is a collection of R games and other funny stuff, such as the
classical Mine sweeper and sliding puzzles.

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
%doc %{rlibdir}/fun/DESCRIPTION
%doc %{rlibdir}/fun/html
%doc %{rlibdir}/fun/NEWS
%{rlibdir}/fun/img
%{rlibdir}/fun/demo
%{rlibdir}/fun/Meta
%{rlibdir}/fun/js
%{rlibdir}/fun/NAMESPACE
%{rlibdir}/fun/R
%{rlibdir}/fun/help
%{rlibdir}/fun/data
%{rlibdir}/fun/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora