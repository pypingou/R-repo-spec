%global packname  crs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.15.8
Release:          1%{?dist}
Summary:          Categorical Regression Splines

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.15-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides for estimating regression splines that handle a mix
of continuous and categorical (discrete) data often encountered in applied
settings. I would like to gratefully acknowledge support from  the Natural
Sciences and Engineering Research Council of Canada (NSERC:www.nserc.ca),
the Social Sciences and Humanities Research Council of Canada
(SSHRC:www.sshrc.ca), and the Shared Hierarchical Academic Research
Computing Network (SHARCNET:www.sharcnet.ca).

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.15.8-1
- initial package for Fedora