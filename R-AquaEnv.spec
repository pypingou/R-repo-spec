%global packname  AquaEnv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          AquaEnv - an integrated development toolbox for aquatic chemical model generation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-minpack.lm R-deSolve 

BuildRequires:    R-devel tex(latex) R-minpack.lm R-deSolve 

%description
AquaEnv is an integrated development toolbox for aquatic chemical model
generation focused on (ocean) acidification and CO2 air-water exchange. It
contains all elements necessary to model the pH, the related CO2 air-water
exchange, as well as aquatic acid-base chemistry in general for an
arbitrary marine, estuarine or freshwater system. Also chemical batches
can be modelled. Next to the routines necessary to calculate desired
information, AquaEnv also contains a suite of tools to visualize this
information. Furthermore, AquaEnv can not only be used to build dynamic
models of aquatic systems, but it can also serve as a simple desktop tool
for the experimental aquatic chemist to generate and visualize all
possible derived information from a set of measurements with one single
easy to use R function. Additionally, the sensitivity of the system to
variations in the input variables can be visualized. The corresponding
publication in Aquatic Geochemistry can be found at

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora