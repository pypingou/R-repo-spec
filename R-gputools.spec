%global packname  gputools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.26
Release:          1%{?dist}
Summary:          A few GPU enabled functions

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides R interfaces to a handful of common statistical
algorithms. These algorithms are implemented in parallel using a mixture
of Nvidia's CUDA langauge, Nvidia's CUBLAS library, and EMI Photonics'
CULA libraries. On a computer equiped with an Nvidia GPU some of these
functions may be substantially more efficient than native R routines.
Thanks to Craig Stark at UC Irvine for donating time on his lab's Mac

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.26-1
- initial package for Fedora