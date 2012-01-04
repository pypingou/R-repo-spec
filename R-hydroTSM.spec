%global packname  hydroTSM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Time series management, analysis and interpolation for hydrological modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-zoo R-xts 

BuildRequires:    R-devel tex(latex) R-zoo R-xts 

%description
S3 functions for management, analysis, interpolation and plotting of time
series used in hydrology and related environmental sciences. In
particular, this package is highly oriented to hydrological modelling
tasks. The focus of this package has been put in providing a collection of
tools useful for the daily work of hydrologists (although an effort was
made to optimise each function as much as possible, functionality has had
priority over speed). Bugs / comments / questions / collaboration of any
kind are very welcomed, and in particular, datasets that can be included
in this package for academic purposes.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora