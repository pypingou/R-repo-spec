%global packname  Animal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Analyze time-coded animal behavior data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The Animal package is a collection of functions for analyzing animal
(including humans) behavior data originating from a variety of sources.
The package has functions to analyze time coded behaviors from CowLog
(open source software for coding behaviors from digital video) data files
and observation files with similar format. Other features include hourly,
daily, weekly and monthly summaries of time coded data, analysis of RIC
(roughage intake system, Insentec automation) data files and labeling
measurement data according to behavioral observations for e.g model
building purposes.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora