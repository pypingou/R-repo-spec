%global packname  spkTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Methods for Spike-in Arrays

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-Biobase R-graphics R-grDevices R-gtools R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-Biobase R-graphics R-grDevices R-gtools R-methods R-RColorBrewer R-stats R-utils 


%description
The package contains functions that can be used to compare expression
measures on different array platforms.

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
%doc %{rlibdir}/spkTools/html
%doc %{rlibdir}/spkTools/DESCRIPTION
%doc %{rlibdir}/spkTools/doc
%{rlibdir}/spkTools/INDEX
%{rlibdir}/spkTools/Meta
%{rlibdir}/spkTools/NAMESPACE
%{rlibdir}/spkTools/data
%{rlibdir}/spkTools/R
%{rlibdir}/spkTools/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora