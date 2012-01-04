%global packname  splots
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Visualization of high-throughput assays in microtitre plate or slide format

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-grid R-RColorBrewer 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-grid R-RColorBrewer 


%description
The splots package provides the plotScreen function for visualising data
in microtitre plate or slide format.

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
%doc %{rlibdir}/splots/DESCRIPTION
%doc %{rlibdir}/splots/html
%doc %{rlibdir}/splots/doc
%{rlibdir}/splots/R
%{rlibdir}/splots/Meta
%{rlibdir}/splots/INDEX
%{rlibdir}/splots/NAMESPACE
%{rlibdir}/splots/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora