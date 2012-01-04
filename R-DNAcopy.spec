%global packname  DNAcopy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          DNA copy number data analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Segments DNA copy number data using circular binary segmentation to detect
regions with abnormal copy number

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
%doc %{rlibdir}/DNAcopy/html
%doc %{rlibdir}/DNAcopy/DESCRIPTION
%doc %{rlibdir}/DNAcopy/doc
%{rlibdir}/DNAcopy/NAMESPACE
%{rlibdir}/DNAcopy/Meta
%{rlibdir}/DNAcopy/benchmark
%{rlibdir}/DNAcopy/CHANGES
%{rlibdir}/DNAcopy/libs
%{rlibdir}/DNAcopy/demo
%{rlibdir}/DNAcopy/help
%{rlibdir}/DNAcopy/R
%{rlibdir}/DNAcopy/data
%{rlibdir}/DNAcopy/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora