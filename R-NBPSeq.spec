%global packname  NBPSeq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          The NBP Negative Binomial Model for Assessing Differential Gene Expression from RNA-Seq

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-qvalue 

BuildRequires:    R-devel tex(latex) R-qvalue 

%description
Fit NBP model to RNA-Seq count data and identify genes differentially
expressing in two groups.

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
%doc %{rlibdir}/NBPSeq/DESCRIPTION
%doc %{rlibdir}/NBPSeq/html
%{rlibdir}/NBPSeq/data
%{rlibdir}/NBPSeq/Meta
%{rlibdir}/NBPSeq/INDEX
%{rlibdir}/NBPSeq/help
%{rlibdir}/NBPSeq/NAMESPACE
%{rlibdir}/NBPSeq/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora