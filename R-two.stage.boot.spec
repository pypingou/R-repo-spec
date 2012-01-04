%global packname  two.stage.boot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Two-stage cluster sample bootstrap algorithm

Group:            Applications/Engineering 
License:          X11
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains a function that implements a bootstrap algorithm for
a two-stage cluster sample due to Rao & Wu (1988).

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
%doc %{rlibdir}/two.stage.boot/DESCRIPTION
%doc %{rlibdir}/two.stage.boot/html
%{rlibdir}/two.stage.boot/R
%{rlibdir}/two.stage.boot/INDEX
%{rlibdir}/two.stage.boot/data
%{rlibdir}/two.stage.boot/Meta
%{rlibdir}/two.stage.boot/help
%{rlibdir}/two.stage.boot/NAMESPACE
%{rlibdir}/two.stage.boot/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora