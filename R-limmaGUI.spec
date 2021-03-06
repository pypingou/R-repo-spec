%global packname  limmaGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          GUI for limma package

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-limma R-tcltk 


BuildRequires:    R-devel tex(latex) R-limma R-tcltk



%description
A Graphical User Interface for the limma Microarray package

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
%doc %{rlibdir}/limmaGUI/doc
%doc %{rlibdir}/limmaGUI/CITATION
%doc %{rlibdir}/limmaGUI/html
%doc %{rlibdir}/limmaGUI/DESCRIPTION
%{rlibdir}/limmaGUI/R
%{rlibdir}/limmaGUI/NAMESPACE
%{rlibdir}/limmaGUI/help
%{rlibdir}/limmaGUI/INDEX
%{rlibdir}/limmaGUI/etc
%{rlibdir}/limmaGUI/Meta
RPM build errors:

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora