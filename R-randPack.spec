%global packname  randPack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Randomization routines for Clinical Trials

Group:            Applications/Engineering 
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-Biobase 


%description
A suite of classes and functions for randomizing patients in clinical

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
%doc %{rlibdir}/randPack/html
%doc %{rlibdir}/randPack/doc
%doc %{rlibdir}/randPack/DESCRIPTION
%{rlibdir}/randPack/data
%{rlibdir}/randPack/R
%{rlibdir}/randPack/NAMESPACE
%{rlibdir}/randPack/Meta
%{rlibdir}/randPack/Scripts
%{rlibdir}/randPack/help
%{rlibdir}/randPack/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora