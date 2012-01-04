%global packname  snowfall
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.84
Release:          1%{?dist}
Summary:          Easier cluster computing (based on snow).

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-snow 

BuildRequires:    R-devel tex(latex) R-snow 

%description
Usability wrapper around snow for easier development of parallel R
programs. This package offers e.g. extended error checks, and additional
functions. All functions work in sequential mode, too, if no cluster is
present or wished. Package is also designed as connector to the cluster
management tool sfCluster, but can also used without it.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.84-1
- initial package for Fedora