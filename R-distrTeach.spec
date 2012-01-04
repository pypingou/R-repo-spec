%global packname  distrTeach
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Extensions of package distr for teaching Stochastics/Statistics in secondary school

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-distr R-distrEx R-startupmsg 

BuildRequires:    R-devel tex(latex) R-methods R-distr R-distrEx R-startupmsg 

%description
Extensions of package distr and some additional functionality

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
%doc %{rlibdir}/distrTeach/NEWS
%doc %{rlibdir}/distrTeach/html
%doc %{rlibdir}/distrTeach/CITATION
%doc %{rlibdir}/distrTeach/DESCRIPTION
%{rlibdir}/distrTeach/R
%{rlibdir}/distrTeach/TOBEDONE
%{rlibdir}/distrTeach/help
%{rlibdir}/distrTeach/INDEX
%{rlibdir}/distrTeach/Meta
%{rlibdir}/distrTeach/demo
%{rlibdir}/distrTeach/NAMESPACE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora