%global packname  margLikArrogance
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Marginal Likelihood Computation via Arrogance Sampling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
In Bayesian statistics, models are evaluated on the basis of data by
comparing their marginal likelihoods conditional on the data.  This
package helps compute models' marginal likelihoods using samples from the
models' posterior parameter distributes (the inputs are similar to those
of the harmonic mean estimator).  The computation itself is done via
"arrogance sampling", a kind of nonparametric (histogram-based) importance

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
%doc %{rlibdir}/margLikArrogance/doc
%doc %{rlibdir}/margLikArrogance/html
%doc %{rlibdir}/margLikArrogance/DESCRIPTION
%{rlibdir}/margLikArrogance/NAMESPACE
%{rlibdir}/margLikArrogance/help
%{rlibdir}/margLikArrogance/Meta
%{rlibdir}/margLikArrogance/INDEX
%{rlibdir}/margLikArrogance/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora