%global packname  oro.nifti
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.8
Release:          1%{?dist}
Summary:          Rigorous - NIfTI+ANALYZE+AFNI Input / Output

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-grDevices R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-graphics R-grDevices R-methods R-utils 

%description
Functions for the input/output and visualization of medical imaging data
that follow either the ANALYZE, NIfTI or AFNI formats.  This package is
part of the Rigorous Analytics bundle.

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
%doc %{rlibdir}/oro.nifti/html
%doc %{rlibdir}/oro.nifti/DESCRIPTION
%doc %{rlibdir}/oro.nifti/CITATION
%doc %{rlibdir}/oro.nifti/doc
%{rlibdir}/oro.nifti/demo
%{rlibdir}/oro.nifti/nifti
%{rlibdir}/oro.nifti/R
%{rlibdir}/oro.nifti/help
%{rlibdir}/oro.nifti/INDEX
%{rlibdir}/oro.nifti/Meta
%{rlibdir}/oro.nifti/NAMESPACE
RPM build errors:
%{rlibdir}/oro.nifti/afni
%{rlibdir}/oro.nifti/anlz

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.8-1
- initial package for Fedora