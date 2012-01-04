%global packname  expert
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Modeling without data using expert opinion

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Expert opinion (or judgment) is a body of techniques to estimate the
distribution of a random variable when data is scarce or unavailable.
Opinions on the quantiles of the distribution are sought from experts in
the field and aggregated into a final estimate. The package supports
aggregation by means of the Cooke, Mendel-Sheridan and predefined weights

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
%doc %{rlibdir}/expert/DESCRIPTION
%doc %{rlibdir}/expert/html
%doc %{rlibdir}/expert/NEWS
%{rlibdir}/expert/NAMESPACE
%{rlibdir}/expert/Meta
%{rlibdir}/expert/INDEX
%{rlibdir}/expert/po
%{rlibdir}/expert/R
%{rlibdir}/expert/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora