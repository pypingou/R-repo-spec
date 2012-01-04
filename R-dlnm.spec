%global packname  dlnm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Distributed Lag Non-linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-stats R-graphics R-grDevices R-utils R-splines R-tsModel 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-stats R-graphics R-grDevices R-utils R-splines R-tsModel 


%description
The package dlnm contains functions to specify basis and cross-basis
matrices in order to run distributed lag models and their non-linear
extension, then to predict and graph the results for a fitted model.

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
%doc %{rlibdir}/dlnm/doc
%doc %{rlibdir}/dlnm/CITATION
%doc %{rlibdir}/dlnm/DESCRIPTION
%doc %{rlibdir}/dlnm/html
%{rlibdir}/dlnm/INDEX
%{rlibdir}/dlnm/Meta
%{rlibdir}/dlnm/NAMESPACE
%{rlibdir}/dlnm/ChangeLog
%{rlibdir}/dlnm/R
%{rlibdir}/dlnm/data
%{rlibdir}/dlnm/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora