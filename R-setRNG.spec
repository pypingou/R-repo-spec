%global packname  setRNG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2009.11.1
Release:          1%{?dist}
Summary:          Set (Normal) Random Number Generator and Seed

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2009.11-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
SetRNG provides utilities to help set and record the setting of the seed
and the uniform and normal generators used when a random experiment is
run. The utilities can be used in other functions that do random
experiments to simplify recording and/or setting all the necessary
information for reproducibility. See the vignette and reference manual for

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
%doc %{rlibdir}/setRNG/DESCRIPTION
%doc %{rlibdir}/setRNG/doc
%doc %{rlibdir}/setRNG/html
%doc %{rlibdir}/setRNG/NEWS
%{rlibdir}/setRNG/help
%{rlibdir}/setRNG/R
%{rlibdir}/setRNG/INDEX
%{rlibdir}/setRNG/LICENSE
%{rlibdir}/setRNG/NAMESPACE
RPM build errors:
%{rlibdir}/setRNG/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2009.11.1-1
- initial package for Fedora