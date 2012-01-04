%global packname  neuRosim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.8
Release:          1%{?dist}
Summary:          Functions to generate fMRI data including activated data, noise data and resting state data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-deSolve 

BuildRequires:    R-devel tex(latex) R-deSolve 

%description
The package allows users to generate fMRI time series or 4D data. Some
high-level functions are created for fast data generation with only a few
arguments and a diversity of functions to define activation and noise. For
more advanced users it is possible to use the low-level functions and
manipulate the arguments.

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
%doc %{rlibdir}/neuRosim/CITATION
%doc %{rlibdir}/neuRosim/DESCRIPTION
%doc %{rlibdir}/neuRosim/html
%{rlibdir}/neuRosim/NAMESPACE
%{rlibdir}/neuRosim/help
%{rlibdir}/neuRosim/INDEX
%{rlibdir}/neuRosim/Meta
%{rlibdir}/neuRosim/R
%{rlibdir}/neuRosim/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.8-1
- initial package for Fedora