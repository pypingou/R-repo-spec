%global packname  gsmoothr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Smoothing tools

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Tools rewritten in C for various smoothing taks

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
%doc %{rlibdir}/gsmoothr/html
%doc %{rlibdir}/gsmoothr/DESCRIPTION
%{rlibdir}/gsmoothr/NAMESPACE
%{rlibdir}/gsmoothr/help
%{rlibdir}/gsmoothr/INDEX
%{rlibdir}/gsmoothr/Meta
%{rlibdir}/gsmoothr/libs
%{rlibdir}/gsmoothr/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora