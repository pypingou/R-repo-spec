%global packname  DEMEtics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.4
Release:          1%{?dist}
Summary:          Evaluating the genetic differentiation between populations based on Gst and D values.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package allows to calculate the fixation index Gst (Nei, 1973) and
the differentiation index D (Jost, 2008) pairwise between or averaged over
several populations. P-values, stating the significance of
differentiation, and 95 percent confidence intervals can be estimated
using bootstrap resamplings. In the case that more than two populations
are compared pairwise, the p-values are adjusted by bonferroni correction
and in several other ways due to the multiple comparison from one data

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
%doc %{rlibdir}/DEMEtics/CITATION
%doc %{rlibdir}/DEMEtics/html
%doc %{rlibdir}/DEMEtics/DESCRIPTION
%{rlibdir}/DEMEtics/NAMESPACE
%{rlibdir}/DEMEtics/data
%{rlibdir}/DEMEtics/INDEX
%{rlibdir}/DEMEtics/R
%{rlibdir}/DEMEtics/help
%{rlibdir}/DEMEtics/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.4-1
- initial package for Fedora