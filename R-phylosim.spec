%global packname  phylosim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.16
Release:          1%{?dist}
Summary:          R packge for simulating biological sequence evolution

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.oo R-ape R-compoisson R-ggplot2 

BuildRequires:    R-devel tex(latex) R-R.oo R-ape R-compoisson R-ggplot2 

%description
PhyloSim is an extensible object-oriented framework for the Monte Carlo
simulation of sequence evolution written in 100 percent R. It is built on
the top of the R.oo and ape packages and uses Gillespie's direct method to
simulate substitutions, insertions and deletions.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.16-1
- initial package for Fedora