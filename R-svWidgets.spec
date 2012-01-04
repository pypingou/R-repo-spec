%global packname  svWidgets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.41
Release:          1%{?dist}
Summary:          SciViews GUI API - Widgets & Windows

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-41.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-tcltk R-utils R-svMisc 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-tcltk R-utils R-svMisc 


%description
High level management of widgets, windows and other graphical resources.

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
%doc %{rlibdir}/svWidgets/CITATION
%doc %{rlibdir}/svWidgets/DESCRIPTION
%doc %{rlibdir}/svWidgets/html
%doc %{rlibdir}/svWidgets/NEWS
%{rlibdir}/svWidgets/INDEX
%{rlibdir}/svWidgets/NAMESPACE
%{rlibdir}/svWidgets/R
%{rlibdir}/svWidgets/Meta
%{rlibdir}/svWidgets/gui
%{rlibdir}/svWidgets/help
%{rlibdir}/svWidgets/LICENSE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.41-1
- initial package for Fedora