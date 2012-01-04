%global packname  BradleyTerry2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.6
Release:          1%{?dist}
Summary:          Bradley-Terry models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-brglm R-gtools R-lme4 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-brglm R-gtools R-lme4 


%description
Specify and fit the Bradley-Terry model and structured versions

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
%doc %{rlibdir}/BradleyTerry2/NEWS
%doc %{rlibdir}/BradleyTerry2/html
%doc %{rlibdir}/BradleyTerry2/CITATION
%doc %{rlibdir}/BradleyTerry2/DESCRIPTION
%doc %{rlibdir}/BradleyTerry2/doc
%{rlibdir}/BradleyTerry2/INDEX
%{rlibdir}/BradleyTerry2/R
%{rlibdir}/BradleyTerry2/help
%{rlibdir}/BradleyTerry2/Meta
%{rlibdir}/BradleyTerry2/NAMESPACE
RPM build errors:
%{rlibdir}/BradleyTerry2/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.6-1
- initial package for Fedora