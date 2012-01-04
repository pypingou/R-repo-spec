%global packname  untb
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.8
Release:          1%{?dist}
Summary:          ecological drift under the UNTB

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-partitions R-Brobdingnag R-polynom 

BuildRequires:    R-devel tex(latex) R-partitions R-Brobdingnag R-polynom 

%description
A collection of utilities for biodiversity data. Includes the simulation
of ecological drift under Hubbell's Unified Neutral Theory of
Biodiversity, and the calculation of various diagnostics such as Preston
curves.  Now includes functionality provided by Francois Munoz and Andrea

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.8-1
- initial package for Fedora