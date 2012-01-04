%global packname  fgui
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Function GUI

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tools 

BuildRequires:    R-devel tex(latex) R-tools 

%description
Rapidly create a GUI interface for a function you created by automatically
creating widgets for arguments of the function. Automatically parses help
routines for context-sensative help to these arguments. The interface
essentially a wrapper to some tcltk routines to both simplify and
facilitate GUI creation. More advanced tcltk routines/GUI objects can be
incorporated into the interface for greater customization for the more

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
%doc %{rlibdir}/fgui/CITATION
%doc %{rlibdir}/fgui/html
%doc %{rlibdir}/fgui/doc
%doc %{rlibdir}/fgui/DESCRIPTION
%{rlibdir}/fgui/INDEX
%{rlibdir}/fgui/Meta
%{rlibdir}/fgui/R
%{rlibdir}/fgui/NAMESPACE
%{rlibdir}/fgui/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora