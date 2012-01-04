%global packname  ringscale
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Ringscale

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-FITSio R-tcltk 

BuildRequires:    R-devel tex(latex) R-FITSio R-tcltk 

%description
Implementation of the "Ringscale" method as proposed in the student
research project "DETECTION OF FAINT COMPANIONS AROUND YOUNG STARS IN
SPECKLE PATTERNS OF VLT/NACO CUBE MODE IMAGES BY MEANS OF POST-PROCESSING"
at the Friedrich-Schiller-University of Jena.

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
%doc %{rlibdir}/ringscale/DESCRIPTION
%doc %{rlibdir}/ringscale/html
%{rlibdir}/ringscale/R
%{rlibdir}/ringscale/Meta
%{rlibdir}/ringscale/INDEX
%{rlibdir}/ringscale/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora