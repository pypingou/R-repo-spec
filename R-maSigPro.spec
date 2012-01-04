%global packname  maSigPro
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Significant Gene Expression Profile Differences in Time Course Microarray Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-Biobase 
Requires:         R-Biobase R-graphics R-grDevices R-limma R-Mfuzz R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-stats R-Biobase
BuildRequires:    R-Biobase R-graphics R-grDevices R-limma R-Mfuzz R-stats R-utils 


%description
maSigPro is a regression based approach to find genes for which there are
significant gene expression profile differences between experimental
groups in time course microarray experiments.

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
%doc %{rlibdir}/maSigPro/html
%doc %{rlibdir}/maSigPro/doc
%doc %{rlibdir}/maSigPro/DESCRIPTION
%{rlibdir}/maSigPro/NAMESPACE
%{rlibdir}/maSigPro/help
%{rlibdir}/maSigPro/Meta
%{rlibdir}/maSigPro/INDEX
%{rlibdir}/maSigPro/data
%{rlibdir}/maSigPro/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora