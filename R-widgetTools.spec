%global packname  widgetTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Creates an interactive tcltk widget

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-tcltk 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-tcltk 

%description
This packages contains tools to support the construction of tcltk widgets

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
%doc %{rlibdir}/widgetTools/DESCRIPTION
%doc %{rlibdir}/widgetTools/html
%doc %{rlibdir}/widgetTools/doc
%{rlibdir}/widgetTools/INDEX
%{rlibdir}/widgetTools/help
%{rlibdir}/widgetTools/Meta
%{rlibdir}/widgetTools/R
%{rlibdir}/widgetTools/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora