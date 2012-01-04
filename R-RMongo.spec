%global packname  RMongo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.21
Release:          1%{?dist}
Summary:          MongoDB Client for R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-methods R-RUnit 

BuildRequires:    R-devel tex(latex) R-rJava R-methods R-RUnit 

%description
MongoDB Database interface for R. The interface is provided via Java calls
to the mongo-java-driver.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.21-1
- initial package for Fedora