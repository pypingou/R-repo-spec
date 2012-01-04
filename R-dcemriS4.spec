%global packname  dcemriS4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.45
Release:          1%{?dist}
Summary:          A Package for Medical Image Analysis (S4 implementation)

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices R-graphics R-methods R-oro.nifti R-utils 

BuildRequires:    R-devel tex(latex) R-grDevices R-graphics R-methods R-oro.nifti R-utils 

%description
A collection of routines and documentation that allows one to perform
voxel-wise quantitative analysis of dynamic contrast-enhanced or
diffusion-weighted MRI data.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.45-1
- initial package for Fedora