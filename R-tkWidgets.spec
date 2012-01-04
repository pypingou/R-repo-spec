%global packname  tkWidgets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          R based tk widgets

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-widgetTools R-DynDoc R-tools 


BuildRequires:    R-devel tex(latex) R-methods R-widgetTools R-DynDoc R-tools



%description
Widgets to provide user interfaces. tcltk should have been installed for
the widgets to run.

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
%doc %{rlibdir}/tkWidgets/doc
%doc %{rlibdir}/tkWidgets/html
%doc %{rlibdir}/tkWidgets/DESCRIPTION
%{rlibdir}/tkWidgets/NAMESPACE
%{rlibdir}/tkWidgets/R
%{rlibdir}/tkWidgets/testfiles
%{rlibdir}/tkWidgets/INDEX
%{rlibdir}/tkWidgets/Meta
%{rlibdir}/tkWidgets/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora