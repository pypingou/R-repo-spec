%global packname  simPopulation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Simulation of synthetic populations for surveys based on sample data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nnet R-POT R-lattice R-vcd 

BuildRequires:    R-devel tex(latex) R-nnet R-POT R-lattice R-vcd 

%description
Simulate populations for surveys based on sample data with special
application to EU-SILC.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora