%global packname  iv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Information Visualisation with UML and Graphs

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-s3x 

BuildRequires:    R-devel tex(latex) R-s3x 

%description
A package for writing technical documentation and visualising discrete
information, using UML diagrams and directed graphs. This package is
replaces the umlr package, plus is incomplete and experimental.

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
%doc %{rlibdir}/iv/DESCRIPTION
%doc %{rlibdir}/iv/html
%doc %{rlibdir}/iv/doc
%{rlibdir}/iv/R
%{rlibdir}/iv/NAMESPACE
RPM build errors:
%{rlibdir}/iv/help
%{rlibdir}/iv/Meta
%{rlibdir}/iv/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora