%global packname  ccTutorial
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.20
Release:          1%{?dist}
Summary:          Data package for ChIP-chip tutorial

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Ringo R-affy R-topGO 

BuildRequires:    R-devel tex(latex) R-Ringo R-affy R-topGO 

%description
This is a data package that accompanies a ChIP-chip tutorial, which has
been published in PLoS Computational Biology. The data and source code in
this package allow the reader to completely reproduce the steps in the

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
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.20-1
- initial package for Fedora