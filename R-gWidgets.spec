%global packname  gWidgets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.47
Release:          1%{?dist}
Summary:          gWidgets API for building toolkit-independent, interactive GUIs

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-47.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils 

%description
gWidgets provides a toolkit-independent API for building interactive GUIs.
Atleast one of the gWidgetsXXX packages, such as gWidgetstcltk, needs to
be installed. Some icons are on loan from the scigraphica project

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
%doc %{rlibdir}/gWidgets/DESCRIPTION
%doc %{rlibdir}/gWidgets/doc
%doc %{rlibdir}/gWidgets/html
%doc %{rlibdir}/gWidgets/NEWS
%{rlibdir}/gWidgets/install
%{rlibdir}/gWidgets/NAMESPACE
%{rlibdir}/gWidgets/help
%{rlibdir}/gWidgets/images
%{rlibdir}/gWidgets/Meta
%{rlibdir}/gWidgets/INDEX
%{rlibdir}/gWidgets/R
RPM build errors:
%{rlibdir}/gWidgets/tests

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.47-1
- initial package for Fedora