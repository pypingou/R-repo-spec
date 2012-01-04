%global packname  samplesize
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          a collection of sample size functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Computes sample size for Student's t-test with equal and nonequal
variances and for the Wilcoxon-Mann-Whitney test for categorical data with
and without ties

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
%doc %{rlibdir}/samplesize/DESCRIPTION
%doc %{rlibdir}/samplesize/html
%{rlibdir}/samplesize/R
%{rlibdir}/samplesize/INDEX
%{rlibdir}/samplesize/Meta
%{rlibdir}/samplesize/NAMESPACE
%{rlibdir}/samplesize/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora