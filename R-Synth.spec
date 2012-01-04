%global packname  Synth
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Synthetic Control Group Method for Comparative Case Studies

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-kernlab R-optimx 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-kernlab R-optimx 


%description
Implements the synthetic control group method for comparative case studies
developed in Abadie and Gardeazabal (2003) and Abadie, Diamond, and
Hainmueller (2010).  The synthetic control method allows for effect
estimation in settings where a single unit (a state, country, firm, etc.)
is exposed to an event or intervention.  It provides a data-driven
procedure to construct synthetic control units based on a weighted
combination of comparison units that approximates the characteristics of
the unit that is exposed to the intervention. A combination of comparison
units often provides a better comparison for the unit exposed to the
intervention than any comparison unit alone.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora