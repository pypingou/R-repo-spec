%global packname  arrayQuality
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Assessing array quality on spotted arrays

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-graphics R-grDevices R-grid R-gridBase R-hexbin R-limma R-marray R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-grid R-gridBase R-hexbin R-limma R-marray R-methods R-RColorBrewer R-stats R-utils 


%description
Functions for performing print-run and array level quality assessment.

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
%doc %{rlibdir}/arrayQuality/html
%doc %{rlibdir}/arrayQuality/doc
%doc %{rlibdir}/arrayQuality/DESCRIPTION
%{rlibdir}/arrayQuality/NAMESPACE
%{rlibdir}/arrayQuality/data
%{rlibdir}/arrayQuality/R
%{rlibdir}/arrayQuality/gprQCData
%{rlibdir}/arrayQuality/help
%{rlibdir}/arrayQuality/INDEX
%{rlibdir}/arrayQuality/Meta
%{rlibdir}/arrayQuality/Heebo
%{rlibdir}/arrayQuality/Meebo

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora