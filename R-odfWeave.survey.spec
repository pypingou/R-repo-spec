%global packname  odfWeave.survey
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Support for odfWeave on the survey package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-odfWeave R-survey 


BuildRequires:    R-devel tex(latex) R-odfWeave R-survey



%description
Provides methods for odfTable() for objects in the survey package.

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
%doc %{rlibdir}/odfWeave.survey/html
%doc %{rlibdir}/odfWeave.survey/DESCRIPTION
%{rlibdir}/odfWeave.survey/R
%{rlibdir}/odfWeave.survey/NAMESPACE
%{rlibdir}/odfWeave.survey/help
%{rlibdir}/odfWeave.survey/INDEX
%{rlibdir}/odfWeave.survey/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora