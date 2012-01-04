%global packname  twslm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          A two-way semilinear model for normalization and analysis of cDNA microarray data.

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-splines 

%description
twslm is for normalization of cDNA microarray data with the two-way
semilinear model. Huber's and Tukey's bisquare weight functions are
available for robust estimation of the two-way semilinear models.

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
%doc %{rlibdir}/twslm/html
%doc %{rlibdir}/twslm/DESCRIPTION
%{rlibdir}/twslm/Meta
%{rlibdir}/twslm/help
%{rlibdir}/twslm/data
%{rlibdir}/twslm/INDEX
%{rlibdir}/twslm/R
%{rlibdir}/twslm/libs
%{rlibdir}/twslm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora